// $(function(){
//   $("button").click(function (){
//     var bntcls = $("button").class("Chartwrapper")

//     if(btncls == )

//   });
// });

$(function(){
  $("#clickmonth").click(function (){
  $("#monthchart").removeClass("Chartwrapper");
  $("#monthtext").removeClass("Chartwrapper");
  $("#causechart").addClass("Chartwrapper");
  $("#causetext").addClass("Chartwrapper");
  $("#timechart").addClass("Chartwrapper");
  $("#timetext").addClass("Chartwrapper");
  $("#weekchart").addClass("Chartwrapper");
  $("#weektext").addClass("Chartwrapper");
  });
  $("#clickcause").click(function () {
  $("#causechart").removeClass("Chartwrapper");
  $("#causetext").removeClass("Chartwrapper");
  $("#monthchart").addClass("Chartwrapper");
  $("#monthtext").addClass("Chartwrapper");
  $("#timechart").addClass("Chartwrapper"); 
  $("#timetext").addClass("Chartwrapper"); 
  $("#weekchart").addClass("Chartwrapper"); 
  $("#weektext").addClass("Chartwrapper"); 
  });
  $("#clickweek").click(function () {
  $("#weekchart").removeClass("Chartwrapper");
  $("#weektext").removeClass("Chartwrapper");
  $("#monthchart").addClass("Chartwrapper");
  $("#monthtext").addClass("Chartwrapper");
  $("#causechart").addClass("Chartwrapper");
  $("#causetext").addClass("Chartwrapper");
  $("#timechart").addClass("Chartwrapper");
  $("#timetext").addClass("Chartwrapper");
  });
  $("#clicktime").click(function () {
  $("#timechart").removeClass("Chartwrapper");
  $("#timetext").removeClass("Chartwrapper");
  $("#monthchart").addClass("Chartwrapper");
  $("#monthtext").addClass("Chartwrapper");
  $("#causechart").addClass("Chartwrapper");
  $("#causetext").addClass("Chartwrapper");
  $("#weekchart").addClass("Chartwrapper");
  $("#weektext").addClass("Chartwrapper");
  });
});
