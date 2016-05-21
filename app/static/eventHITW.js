function EventHITW(event_id, event_title, event_location, event_start_tee_time, event_end_tee_time, event_date) {
  this.event_id = event_id;
  this.event_title = event_title;
  this.event_location = event_location;
  this.event_start_tee_time = event_start_tee_time;
  this.event_end_tee_time = event_end_tee_time;
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
  this.get_event_start_tee_time = function() {
    return this.event_start_tee_time;
  }
  this.get_event_end_tee_time = function() {
    return this.event_end_tee_time;
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
  this.set_event_start_tee_time = function(event_start_tee_time) {
    this.event_start_tee_time = event_start_tee_time;
  }
  this.set_event_end_tee_time = function(event_end_tee_time) {
    this.event_end_tee_time = event_end_tee_time;
  }
  this.set_event_date = function(event_date) {
    this.event_date = event_date;
  }
  this.jsonify = function() {
    var jsonData = {
      "identifier":   this.get_event_id(),
      "title":        this.get_event_title(),
      "location":     this.get_event_location(),
      "startTeeTime": this.get_event_end_tee_time(),
      "endTeeTime":   this.get_event_end_tee_time(),
      "date":         this.get_event_date()
    }
    return JSON.stringify(jsonData);
  }
}
