angular.module("yoFeul")
    .config(function ($routeProvider) {

        $routeProvider.when("/register", {
            templateUrl: "views/resigter.html"
        });

        $routeProvider.otherwise({
            templateUrl: "views/login.html"
        });
    })