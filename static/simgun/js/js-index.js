/**
 * Created by Negin on 1/13/2017.
 */


$(document).ready(function() {
    $(function() {
        $('.special.cards .image').dimmer({
            on: 'hover'
        });

        $('#reading-progress').progress();

        $('.carousel').flickity({
            // options
            cellAlign: 'left',
            wrapAround : true,
            draggable: false,
            // contain: true,
            autoPlay: 4000,
            // imagesLoaded: true,
            percentPosition: false,
        });

    });
});
