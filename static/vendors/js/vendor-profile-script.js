$(function () {
    $('.menu .item')
        .tab();
});

$('#single-modal')
    .modal('attach events', '#single-book', 'show')
    .modal('attach events', '#single-cancel', 'cancel')
    .modal('attach events', '#single-cancel', function () {
        $(this).find("input,textarea").val('').end();
    })
;
$('#multiple-modal')
    .modal('attach events', '#multiple-book', 'show')
    .modal('attach events', '#multiple-cancel', 'cancel')
;

$('#add-book-submit').click(function() {
    document.getElementById('add-book-form').submit();
});



$('#setting-modal')
    .modal('attach events', '.setting-book', 'show')
    .modal('attach events', '#setting-cancel', 'cancel')
;