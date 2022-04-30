/* eslint-disable no-undef */

const fs = require("fs");
const path = require("path");

const staticSrc = path.resolve(__dirname, "..", "src", "static", "vue");
const templatesSrc = path.resolve(__dirname, "..", "src", "templates", "vue");

fs.rmSync(staticSrc, { recursive: true, force: true });
fs.rmSync(templatesSrc, { recursive: true, force: true });

fs.mkdirSync(staticSrc);
fs.mkdirSync(templatesSrc);

const distSrc = path.resolve(__dirname, "dist");

fs.cpSync(
  path.resolve(distSrc, "favicon.ico"),
  path.resolve(templatesSrc, "favicon.ico")
);
fs.cpSync(
  path.resolve(distSrc, "index.html"),
  path.resolve(templatesSrc, "index.html")
);
copyDirSync(path.resolve(distSrc, "static", "vue"), staticSrc);

function copyDirSync(src, dest) {
  let entries = fs.readdirSync(src, { withFileTypes: true });

  for (let entry of entries) {
    let srcPath = path.join(src, entry.name);
    let destPath = path.join(dest, entry.name);

    entry.isDirectory()
      ? copyDirSync(srcPath, destPath)
      : fs.copyFileSync(srcPath, destPath);
  }
}
