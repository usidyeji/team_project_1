
$(document).ready(function () {
  $('.gauge').each(function () {
      var $this = $(this);
      var per = $this.attr('per');
      $this.animate({
          width: per + "%"
      });
  });
});