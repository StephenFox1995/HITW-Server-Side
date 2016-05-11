function addGallery(element, images) {
  if (images instanceof Array) {
    $(element).append(galleryBody());

    images.forEach(function(image) {
      $('.row').append(galleryItem(image));
    });
  }
}

// Returns the ccs for a gallery item.
function galleryItem(url) {
  return '<li class="col-lg-6 col-md-6 col-sm-6 col-xs-6">' +
            '<img class="thumbnail img-responsive" src="' + url + '">' +
         '</li>';
}

// Reuturns the css for a gallery item.
function galleryBody() {
  var body =
      '<h1>Gallery</h1>' +
      '<ul class="row" style="display:inline-block"></ul>'
  return body;
}
