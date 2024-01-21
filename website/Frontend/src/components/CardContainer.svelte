<!-- src/components/CardContainer.svelte -->

<script>
    // Define the props for the CardContainer component
    import Card from './card.svelte'
    export let cards;
    export let onSelectCity; 
</script>

<style>
    /* Styling for the card container */
    .card-container {
        display: flex;
        overflow-x: auto; /* Enable horizontal scrollbar if needed */
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 16px;
        margin: 16px;
    }
</style>

<div class="card-container">
    <!-- Render individual Card components within the container -->
    {#each cards as card (card.id)}
        <Card
            title={card.title}
            description={card.description}
            cardId = {card.id}
            onCardSelect={onSelectCity}
        />
    {/each}
</div>
