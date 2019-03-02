angular.module("yoFeul",["ngRoute"])
    .controller("generalCtrl", function($scope) {
        $scope.isSignedIn = false;
        $scope.username = "Login";

        $scope.setUsername = function(name){
            $scope.username=name;
        }
    })