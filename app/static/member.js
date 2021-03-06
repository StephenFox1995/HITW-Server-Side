function Member(member_id, member_f_name, member_l_name, member_handicap) {
  this.member_id = member_id;
  this.member_f_name = member_f_name;
  this.member_l_name = member_l_name;
  this.member_handicap = member_handicap;

  this.get_member_id = function() {
    return this.member_id;
  }
  this.get_member_f_name = function() {
    return this.member_f_name;
  }
  this.get_member_l_name = function() {
    return this.member_l_name;
  }
  this.get_member_handicap = function() {
    return this.member_handicap;
  }
  this.set_member_id = function(member_id) {
    this.member_id = member_id;
  }
  this.set_member_f_name = function(member_f_name) {
    this.member_f_name = member_f_name;
  }
  this.set_member_l_name = function(member_l_name) {
    this.member_l_name = member_l_name;
  }
  this.set_member_handicap = function(member_handicap) {
    this.member_handicap = member_handicap;
  }

  this.get_member_fullname = function() {
    return this.member_f_name + ' ' + this.member_l_name;
  }
  this.jsonify = function() {
    var jsonData = {
      "firstname" :this.get_member_f_name(),
      "lastname"  :this.get_member_l_name(),
      "handicap"  :this.get_member_handicap(),
      "identifier":this.get_member_id()
    }
    return JSON.stringify(jsonData);
  }
}
