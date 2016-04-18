function Result(event_id, member_id, result_score) {
  this.event_id = event_id;
  this.member_id = member_id;
  this.result_score = result_score;

  this.get_member_id = function() {
    return this.member_id;
  }
  this.get_event_id = function() {
    return this.event_id;
  }
  this.get_result_score = function() {
    return this.result_score;
  }
}
