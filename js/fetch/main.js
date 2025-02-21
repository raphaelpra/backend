const response = await fetch("https://example.com", {
  verbose: true,
});
console.log(await response.text())
