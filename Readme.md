BookMyMovie is a Movie Booking application which will allow to book tickets for users 

Functional Requirements: 
    1. User can be Created 
    2. User can login -- Home page  
    3. User can choose city.
    4. User can choose Movie.
    5. User can choose Theatre.
    6. List all shows in chosen Theatre with Show Timings and Available seats.
    7. User Should able to Book any number tickets if available for any show. 


                                    
Non-Functional Requirements: 
    - Scalability: We can scale Horizontally/Vertically 
    - Availability: System should be available
    - Performance: 
    - Latency: 
    - Throughput:
    - Security: Not much required -> User cannot access to other user's resources and details.
    - Fault Tollerance: []->[]


DB schema

Tables
    User
        - id 
        - name
        - email 
        - phone

    City - [array of cities]

    Movie 
        - id
        - title
        - desc 
        - length
        - genre

    Theatre
        - id
        - name 
        - city

    Screen 
        - id 
        - theatreId
        - seats

    Show 
        - id 
        - theatreId 
        - DateTime
        - screenId
        - MovieId
        - Price

    Tickets 
        - id
        - userId
        - showid
        - numberOfTickets

Flow

    User Logged In ----> User Select City from Listed ones 

1. Fetch Theatres from `city` 
    - Select * from Theatres where city == `city`; 

2. Fetch Movie and respective show times from theatre_id based on Date.
    SELECT Show.* , Movie.* 
    FROM Show 
    JOIN Movie ON Show.MovieId = Movie.id 
    WHERE Show.theatreId = `theatre_id`
      AND Show.DateTime BETWEEN `your_start_date` AND `your_end_date`;

3. When Selected show, Fetch available seats on that show and process Booking. 
    Select * from Screen where id == `show.screenId`
    // check if we have enough seats  -> procees to Booking 



Routes:
    /user
        /createUser - POST
        /getUser 

    /auth
        /login - POST
        /logout
        
    /movie
        /getAllMovies
        /getTheatresFromCity
        /getMoviesAndShowsFromTheatreId
        /getShow
        /bookshow - POST





