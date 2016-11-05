$(document).ready(function(){

  var owl = $('#owl-demo');

  owl.owlCarousel({
        autoPlay: true,
        items: 2, // items above 1000px browser width
        itemsDesktop: [1000, 2], // 2 items between 1000px and 901px
        itemsDesktopSmall: [900, 2], // 2 items betweem 900px and 601px
        itemsTablet: [600, 1], // 2 items between 600px and 480px
        itemsMobile: [479,1] // 1 item between 479px and 0px
    });
    // Custom Navigation Events
    $(".next").click(function() {
        owl.trigger('owl.next');
    })
    $(".prev").click(function() {
        owl.trigger('owl.prev');
    })
});
