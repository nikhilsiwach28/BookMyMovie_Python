<!-- src/components/DatePicker.svelte -->

<script>
    // Define the props for the DatePicker component
    export let onSelectDate;
</script>

<style>
    /* Styling for the date picker */
    .date-picker {
        display: flex;
        justify-content: space-around;
        margin: 16px;
    }

    .date-button {
        padding: 8px;
        cursor: pointer;
        border: 1px solid #ddd;
        border-radius: 4px;
        background-color: #fff;
    }

    .date-button:hover {
        background-color: #f0f0f0;
    }
</style>

<div class="date-picker">
    <!-- Render date buttons for today to 7 days in the future -->
    {#each Array.from({ length: 8 }).map((_, index) => new Date(new Date().getTime() + index * 24 * 60 * 60 * 1000).toDateString()) as date}
        <div on:click={() => onSelectDate(date)} class="date-button">
            {date}
        </div>
    {/each}
</div>
