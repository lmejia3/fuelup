angular.module("yoFeul",["ngRoute"])
    .controller("generalCtrl", function($scope) {
        $scope.isSignedIn = false;
        $scope.username = null;
    })