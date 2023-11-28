const { ESLint } = require("eslint");
const path = require("path");
const fs = require("fs").promises;

async function lintFiles(directoryPath) {
  const eslint = new ESLint({
    overrideConfigFile: path.resolve(
      __dirname,
      "..",
      "config",
      ".eslintrc.json"
    ),
    ignore: false,
  });

  async function getJavaScriptFiles(dir) {
    let files = await fs.readdir(dir);
    files = await Promise.all(
      files.map(async (file) => {
        const filePath = path.resolve(dir, file);
        const stat = await fs.stat(filePath);
        return stat.isDirectory() ? getJavaScriptFiles(filePath) : filePath;
      })
    );
    return files.flat().filter((file) => file.endsWith(".js"));
  }

  const codeFiles = await getJavaScriptFiles(
    directoryPath || path.resolve(__dirname, "..", "testFiles")
  );

  try {
    const results = await eslint.lintFiles(codeFiles);
    const formatter = await eslint.loadFormatter(); // Load the formatter
    const formattedResults = formatter.format(results); // Format the results
    console.log(formattedResults);
  } catch (error) {
    console.error(error);
    process.exitCode = 1;
  }
}

lintFiles();
