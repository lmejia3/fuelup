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
        $routeProvider.when("/user/quote/received", {
            templateUrl: "views/user_quote_reciept.html"
        });
        $routeProvider.when("/agent/requests", {
            templateUrl: "views/agent_requests.html"
        });
        $routeProvider.when("/agent/rates", {
            templateUrl: "views/agent_rates.html"
        });
        $routeProvider.when("/agent/profile", {
            templateUrl: "views/agent_profile.html"
        });
        $routeProvider.when("/agent/transactions", {
            templateUrl: "views/agent_transactions.html"
        });
        $routeProvider.otherwise({
            templateUrl: "views/login.html"
        });
    })