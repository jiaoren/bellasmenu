$(document).ready(function(){
  $("#search_button").click(function(){
     $("#searchform").unbind('submit').submit();
     
  });
});

$(document).ready(function () {
  $("#query").autocomplete(
     '/ajax/search/autocomplete/',
     {multiple: true, multipleSeparator: ' '}
  );
});