/******/ (() => { // webpackBootstrap
/*!*****************************!*\
  !*** ./assets/js/custom.js ***!
  \*****************************/
window.addEventListener("load", () => {
  hero_video = document.getElementById("hero_video");
  video_link = hero_video.children[1].href;
  console.log("the link : ", video_link);
  hero_video.src = video_link;
  hero_video.innerHTML = `
    <source src="${video_link}" type="video/mp4">
    <source src="${video_link}" type="video/webm">
    Your browser does not support the video tag.
  `;
  hero_video.load();
  try {
    hero_video.play();
  } catch (exception) {
    console.error("error playing video: ", exception);
  }
});

/******/ })()
;
//# sourceMappingURL=custom.js.map