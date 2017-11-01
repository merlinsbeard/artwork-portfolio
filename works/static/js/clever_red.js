 $(document).ready(function(){
  $('.parallax').parallax();
});


  lightGallery(document.getElementById('animated-thumb'), {
          thumbnail:true,
          animateThumb: false,
          showThumbByDefault: false
  }); 

var simplemde1 = new SimpleMDE({ element: document.getElementById("id_description") });
var simplemde2 = new SimpleMDE({ element: document.getElementById("id_long_description") });
