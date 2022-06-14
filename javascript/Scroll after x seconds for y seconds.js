setTimeout(() => {
            $('html:not(:animated), body:not(:animated)').animate({
            scrollTop: $("#target").offset().top
        }, 30000); // scroll for 30 seconds (long)


}, 10000) // start scrolling after 10 seconds

