function addGallery(element, images) {
  if (images instanceof Array) {
    $(element).append(galleryBody());

    images.forEach(function(image) {
      $('.row').append(galleryItem(image));
    });
  }
}

// Returns the ccs for a gallery item.
function galleryItem(src) {
  return '<li class="col-lg-2 col-md-2 col-sm-3 col-xs-4">' +
            '<img class="img-responsive" src="' + src + '">' +
         '</li>';
}

// Reuturns the css for a gallery item.
function galleryBody() {
  var body =
      '<h1>Gallery</h1>' +
      '<ul class="row" style="width: inherit;"></ul>'

  return body;
}
