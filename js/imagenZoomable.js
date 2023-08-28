document.addEventListener('DOMContentLoaded', function() {
  const imageContainer = document.querySelector('.image-container');
  const zoomImage = document.querySelector('.zoom-image');

  imageContainer.addEventListener('click', function(e) {
    if (zoomImage.classList.contains('zoomed')) {
      zoomImage.classList.remove('zoomed');
    } else {
      const { left, top, width, height } = this.getBoundingClientRect();
      const x = e.clientX - left;
      const y = e.clientY - top;
      const xPercent = (x / width) * 100;
      const yPercent = (y / height) * 100;

      zoomImage.style.transformOrigin = `${xPercent}% ${yPercent}%`;
      zoomImage.classList.add('zoomed');

      this.addEventListener('mousemove', function(e) {
        const x = e.clientX - left;
        const y = e.clientY - top;
        const xPercent = (x / width) * 100;
        const yPercent = (y / height) * 100;
        zoomImage.style.transformOrigin = `${xPercent}% ${yPercent}%`;
      });
    }
  });
  const mouseMoveHandler = function(e) {
    const x = e.clientX - left;
    const y = e.clientY - top;
    const xPercent = (x / width) * 100;
    const yPercent = (y / height) * 100;
    zoomImage.style.transformOrigin = `${xPercent}% ${yPercent}%`;
  };
  imageContainer.addEventListener('mouseleave', function() {
    zoomImage.classList.remove('zoomed');
    this.removeEventListener('mousemove', mouseMoveHandler);
  });
});
