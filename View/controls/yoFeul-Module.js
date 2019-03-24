angular.module("yoFeul",["ngRoute"])
    .controller("generalCtrl", function($scope, loginService) {
        $scope.username = "Login";

        $scope.updateName = function(){
            $scope.username= loginService.username;
        }
    })