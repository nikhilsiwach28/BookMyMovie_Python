<script>
    import Header from './Header.svelte';
    import CardContainer from './CardContainer.svelte';
    import DatePicker from './DatePicker.svelte';
    let cities = [
            { id: 1, title: "Delhi"},
            { id: 2, title: "Noida" },
            { id: 3, title: "Gurugram" },
            { id: 4, title: "Faridabad" },
            { id: 5, title: "Ghaziabad" },
            { id: 6, title: "Mumbai" },
            { id: 7, title: "Bangaluru" },
            { id: 8, title: "Pune" },
            { id: 9 , title: "Hyderabad"},
            { id: 10 , title: "Kolkata"}
            // Add more cards as needed
        ];

    let selectedCity;
    let showCityDetails = false;

    // Handle city selection
    function handleCitySelection(cityId) {
        console.log("cityid", cityId)
        selectedCity = cityId;
        showCityDetails = true;
    }

    function onSelectDate(date){
        console.log("date:",date)
    }
</script>

<main>
    <Header></Header>
    <h3>Select City</h3>

    <CardContainer cards={cities} onSelectCity={handleCitySelection} />

    <!-- Render city details when a city is selected -->
    {#if showCityDetails}
        <DatePicker onSelectDate={onSelectDate} />
    {/if}

    <h3>Current Screening Movies</h3>

    <CardContainer 
        cards={[
            { id: 1, title: "Movie 1", description: "Description for Movie 1" },
            { id: 2, title: "Movie 2", description: "Description for Movie 2" },
            { id: 3, title: "Movie 2", description: "Description for Movie 2" },
            { id: 4, title: "Movie 2", description: "Description for Movie 2" },
            { id: 5, title: "Movie 2", description: "Description for Movie 2" },
            { id: 6, title: "Movie 2", description: "Description for Movie 2" },
            { id: 7, title: "Movie 2", description: "Description for Movie 2" },
            { id: 8, title: "Movie 2", description: "Description for Movie 2" }
            // Add more cards as needed
        ]}
    />

</main>

<style>

</style>