$(document).ready(function () {
    var hash = window.location.hash;
    if (hash === '#readingprograms') {
        $('#readingprogram-header').addClass('active', 'back-grey');
        $('#readingprogram-tab').addClass('active');
    } else if (hash === '#favlist') {
        $('#favlist-header').addClass('active', 'back-grey');
        $('#favlist-tab').addClass('active');
    } else if (hash === '#reviews') {
        $('#reviews-header').addClass('active', 'back-grey');
        $('#reviews-tab').addClass('active');
    } else if (hash === '#ordershistory') {
        $('#ordershistory-header').addClass('active', 'back-grey');
        $('#ordershistory-tab').addClass('active');
    } else {
        $('#favlist-header').addClass('active', 'back-grey');
        $('#favlist-tab').addClass('active');
    }

});