/**
 * Created by Negin on 1/8/2017.
 */

$(document).ready(function() {
    $('.ui.menu a.item').on('click', function() {
        $(this)
            .addClass('active')
            .siblings('.item')
            .removeClass('active');
    });
    $('#support-modal')
        .modal('attach events', '#support-button', 'show')
        .modal('attach events', '#ticket-cancel', 'cancel')
    ;
});