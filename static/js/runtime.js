function run_slideshow(md_file) {

  console.log(`running slideshow ${md_file}`);
  const slideshow = remark.create({
    ratio: "16:9",
    countIncrementalSlides: false,
    highlightLines: true,
    sourceUrl: md_file,
  });

  // shift-space = previous slide
  document.addEventListener("keydown", function (event) {
    if (event.shiftKey && event.code === "Space") {
      event.preventDefault();
      event.stopImmediatePropagation();
      slideshow.gotoPreviousSlide();
    }
  });

  // command -> = last slide
  document.addEventListener("keydown", function (event) {
    if (event.metaKey && event.code === "ArrowRight") {
      event.preventDefault();
      event.stopImmediatePropagation();
      slideshow.gotoLastSlide();
    }
  });

  // command <- = first slide
  document.addEventListener("keydown", function (event) {
    if (event.metaKey && event.code === "ArrowLeft") {
      event.preventDefault();
      event.stopImmediatePropagation();
      slideshow.gotoFirstSlide();
    }
  });
}

// expose globally so we can use it in the global context (e.g. from the HTML)
console.log("exposing run_slideshow globally");
window.run_slideshow = run_slideshow;
