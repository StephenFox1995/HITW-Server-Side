function EventHITW(event_id, event_title, event_location, event_time, event_date) {
  this.event_id = event_id;
  this.event_title = event_title;
  this.event_location = event_location;
  this.event_time = event_time;
  this.event_date = event_date;

  // Getters
  this.get_event_id = function() {
    return this.event_id;
  }
  this.get_event_title = function() {
    return this.event_title;
  }
  this.get_event_location = function() {
    return this.event_location;
  }
  this.get_event_time = function() {
    return this.event_time;
  }
  this.get_event_date = function() {
    return this.event_date;
  }
  // Setters
  this.set_event_id = function(event_id) {
    this.event_id = event_id;
  }
  this.set_event_title = function(event_title) {
    this.event_title = event_title;
  }
  this.set_event_location = function(event_location) {
    this.event_location = event_location;
  }
  this.set_event_time = function(event_time) {
    this.event_time = event_time;
  }
  this.set_event_date = function(event_date) {
    this.event_date = event_date;
  }
  this.jsonify = function() {
    var jsonData = {
      "identifier" :this.get_event_id(),
      "title"  :this.get_event_title(),
      "location"  :this.get_event_location(),
      "time":this.get_event_time(),
      "date": this.get_event_date()
    }
    return JSON.stringify(jsonData);
  }
}
