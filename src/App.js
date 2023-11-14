const { ESLint } = require("eslint");
const path = require("path");

async function lintFiles() {
  const eslint = new ESLint({
    overrideConfigFile: path.resolve(
      __dirname,
      "..",
      "config",
      ".eslintrc.json"
    ),
    ignore: false,
  });

  const codeFiles = [path.resolve(__dirname, "..", "testFiles", "test1.js")];

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
