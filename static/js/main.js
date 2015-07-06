var mainApp = angular.module('mainApp', ['ngRoute']);
var host = '/static/';

mainApp.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});

mainApp.controller('BaseCtrl', function ($scope, $http, $location) {
    $scope.matches = [];
    $http.get('/matches')
        .success(function (data) {
            console.log(data);
            $scope.matches = data.matches;
        });

    $scope.edit = function (match) {
          $location.path('/matches/' + match.match_id + '/edit/');
    };
});

mainApp.controller('MatchCtrl', function ($scope, $http, $routeParams) {
    $scope.matchId = $routeParams.matchId;
    $http.get('/matches/' + $scope.matchId)
        .success(function (data) {
            $scope.match_data = data;
        });

});

mainApp.controller('UserCtrl', function ($scope, $http, $routeParams) {
     $scope.userId = $routeParams.userId;

     $http.get('/users/' + $scope.userId)
        .success(function (data) {
            $scope.user_data = data;
        });
});

mainApp.controller('NewMatchCtrl', function ($scope, $http, $location) {
    $http.get('/users')
        .success(function (data) {
            $scope.users = data.users;
        });

    $scope.submit = function () {
        var dump = {
            "match_time": $scope.match_time,
            "users": $scope.match_users,
            "game": 1,
            "score": $scope.score,

        };
        console.log(dump);
        $http.post('/matches/new/', dump)
            .success(function (data) {
                $location.path('/');
            });
    };

});

mainApp.controller('EditMatchCtrl', function ($scope, $http, $location, $routeParams, $filter) {
    $scope.matchId = $routeParams.matchId;
    $http.get('/users')
        .success(function (data) {
            $scope.users = data.users;
            $http.get('/matches/' + $scope.matchId)
                .success(function (data) {
                    console.log(data);
                    $scope.match_time = new Date(data.match_time);
                    $scope.match_users = data.users;
                    $scope.score = data.score;
                    // $scope.match_time = data.users;
                });

        });
    
    $scope.submit = function () {
        var dump = {
            "match_time": $scope.match_time,
            "users": $scope.match_users,
            "game": 1,
            "score": $scope.score,

        };
        console.log(dump);
        $http.post('/matches/edit/' + $scope.matchId, dump)
            .success(function (data) {
                $location.path('/');
            });
    };

});