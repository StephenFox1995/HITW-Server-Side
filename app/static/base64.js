File.prototype.convertToBase64 = function(callback) {
  var file_reader = new FileReader();
  file_reader.onload = function(e) {
    callback(e.target.result);
  }
  file_reader.readAsDataURL(this);
}
