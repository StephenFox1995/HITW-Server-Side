function addGallery(element, images) {
  if (images instanceof Array) {
    $(".container").append(galleryBody());

    images.forEach(function(image) {
      $('.row').append(galleryItem(image));
    });
  }
}

// Returns the ccs for a gallery item.
function galleryItem(url) {
  return '<div class="col-lg-3 col-sm-4 col-xs-6"><a title="Image 1" href="#"><img class="thumbnail img-responsive" src="//placehold.it/600x350"></a></div>';
}

function galleryBody() {
  var body =
      '<h1>Gallery</h1>' +
      '<div class="row"></div>'
  return body;
}
