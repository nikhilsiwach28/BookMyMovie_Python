<!-- src/components/Card.svelte -->

<script>
    // Define the props for the Card component
    export let title;
    export let description = "";
    export let onCardSelect;
    export let cardId;

    function handlerCardOnClick(){
        onCardSelect(cardId)
    }
</script>

<style>
    /* Styling for the individual card */
    .card {
        flex: 0 0 auto; /* Allow the card to grow horizontally */
        max-width: 300px; /* Set a maximum width if needed */
        padding: 25px;
        background-color: #eeeaea;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        margin-right: 16px;
    }
</style>

<div style ="cursor: {onCardSelect ? 'pointer' : 'not-allowed'}"on:click={handlerCardOnClick} class="card">
    <!-- Card content goes here -->
    <h3>{title}</h3>
    <p>{description}</p>
</div>
