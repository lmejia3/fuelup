angular.module("yoFeul")
    .config(function ($routeProvider) {

        $routeProvider.when("/register", {
            templateUrl: "views/register.html"
        });
        $routeProvider.when("/login", {
            templateUrl: "views/login.html"
        });
        $routeProvider.when("/user", {
            templateUrl: "views/user_main.html"
        });
        $routeProvider.when("/user/profile", {
            templateUrl: "views/user_profile.html"
        });
        $routeProvider.when("/user/history", {
            templateUrl: "views/user_history.html"
        });
        $routeProvider.when("/user/quote", {
            templateUrl: "views/user_quote.html"
        });
        $routeProvider.when("/user/invoices", {
            templateUrl: "views/user_invoices.html"
        });
        $routeProvider.when("/getpass", {
            templateUrl: "views/forgotpassword.html"
        });
        $routeProvider.when("/about", {
            templateUrl: "views/about.html"
        });
        $routeProvider.otherwise({
            templateUrl: "views/login.html"
        });
    })