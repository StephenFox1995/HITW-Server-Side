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
}
