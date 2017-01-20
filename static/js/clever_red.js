 $(document).ready(function(){
  $('.parallax').parallax();
});

var $grid = $('.grid').masonry({
	  itemSelector: '.grid-item',
	  percentPosition: true,
	  columnWidth: 100,
	gutter: 10
	});
	// layout Isotope after each image loads
	$grid.imagesLoaded().progress( function() {
	  $grid.masonry();
	});


  // Initialize collapse button
  $(".button-collapse").sideNav();
  // Initialize collapsible (uncomment the line below if you use the dropdown variation)
  //$('.collapsible').collapsible();
