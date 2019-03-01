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
        $routeProvider.otherwise({
            templateUrl: "views/login.html"
        });
    })