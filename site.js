// Photo galleries: clicking a thumbnail swaps the large photo.
document.querySelectorAll('.gallery').forEach(function (gallery) {
  var main = gallery.querySelector('.gallery__main img');
  gallery.querySelectorAll('.thumb').forEach(function (thumb) {
    thumb.addEventListener('click', function () {
      main.src = thumb.dataset.src;
      main.alt = thumb.dataset.alt;
      gallery.querySelectorAll('.thumb').forEach(function (t) {
        t.classList.toggle('is-on', t === thumb);
      });
    });
  });
});
