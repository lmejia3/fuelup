angular.module("yoFeul", ["ngRoute"])
    .controller("generalCtrl", function ($scope, loginService, $window) {
        $scope.username = "Login";
        $scope.type = "";
        $scope.updateName = function () {
            $scope.username = loginService.username;
            $scope.type = loginService.type;
            $scope.loggedIn = true;
        }

        $scope.info = [];

        $scope.loggedIn = false;

        $scope.Today = function () {
            return new Date();
        }

        var lg = loginService;
        $scope.logout = function () {
            console.log('reset');
            lg.password = "";
            lg.key = ""
            lg.id = ""
            lg.type = "";
            lg.loggedIn = false;
            $scope.loggedIn = false;
            $scope.username = "Login";

            window.location = "#!home"
            $window.location.reload();
        }
    })