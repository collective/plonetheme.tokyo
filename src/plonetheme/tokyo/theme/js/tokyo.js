if (window.jQuery) {
  define('jquery', [], function() {
    'use strict';
    return window.jQuery;
  });
}

require([
  'mockup-patterns-textareamimetypeselector',
  'mockup-patterns-relateditems',
  'mockup-patterns-querystring',
  'mockup-patterns-tinymce',
  'mockup-patterns-inlinevalidation',
  'mockup-patterns-structure',
  'mockup-patterns-structureupdater',
  'mockup-patterns-recurrence',
  'plone-patterns-portletmanager',
  'plone-patterns-toolbar',
], function() {
  'use strict';
});

(function($) {
  'use strict'; // Start of use strict

  $(document).ready(function() {

    // Custom JavaScript

  });

})(jQuery); // End of use strict
