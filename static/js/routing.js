mainApp.config(function($routeProvider, $locationProvider) {
  $routeProvider
   .when('/', {
    templateUrl: host + 'templates/base.html',
    controller: 'BaseCtrl',
  })
   .when('/matches/new', {
      templateUrl: host + 'templates/new_match.html',
      controller: 'NewMatchCtrl'
  })
  .when('/matches/edit/:matchId', {
      templateUrl: host + 'templates/new_match.html',
      controller: 'EditMatchCtrl'
  })
  .when('/matches/:matchId', {
    templateUrl: host + 'templates/match.html',
    controller: 'MatchCtrl'
  })
  .when('/matches', {
      templateUrl: host + 'templates/matches.html',
      controller: 'MatchesCtrl'
  })
  .when('/users/:userId', {
    templateUrl: host + 'templates/users.html',
    controller: 'UserCtrl'
  })

  ;

});