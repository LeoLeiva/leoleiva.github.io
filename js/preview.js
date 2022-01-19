/*------------------------------------
 *Author:FortunaTheme
 *Template:Rivo
 *Version:1.1
 *-------------------------------------
 */
(function($) {

    "use strict";

    jQuery(document).on("ready", function() {



        /*
         * -----------------------------------------------------------------
         *---------------------------Preloader and Anchor Tag---------------
         * -----------------------------------------------------------------
         */

        var themeWindow = $(window);
        var pagebody = $('html, body');
        themeWindow.on("load", function() {

            var preloader = jQuery('.preloader');
            var preloaderArea = jQuery('.preloader-area');
            preloader.fadeOut();
            preloaderArea.delay(200).fadeOut('slow');
            themeWindow.scrollTop(0);
        });

        var anchor = $('a[href="#"]');
        anchor.on("click", function() {
            e.preventDefault();
        });



    });

})(jQuery);