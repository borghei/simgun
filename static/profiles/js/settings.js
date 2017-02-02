$(document).ready(function() {
    $(function () {
        $('#address-button').click(function () {
            $('#address-field').toggle("slow");
        });
        $( "#close-icon-show" )
            .on("mouseenter", function() {
                $("#close-icon").show("slow");
                $("#close-icon").click(function () {
                //    TODO delete the address field
                })
            })
            .on("mouseleave", function() {
                $("#close-icon").hide("slow");
            });
    });

});