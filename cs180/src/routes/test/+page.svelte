<script>
  let imageFile;
  let imagePreview = null;
  let file;
  let prediction = '';
  let loading = false;

  function handleFileChange(event) {
    file = event.target.files[0];
    if (file && file.type.startsWith("image/")) {
      imageFile = file;
      const reader = new FileReader();
      reader.onload = (e) => {
        imagePreview = e.target.result;
      };
      reader.readAsDataURL(file);
    } else {
      imagePreview = null;
    }
  }

  async function handleSubmit() {
    if (!file) return;

    const formData = new FormData();
    formData.append('image', file);

    loading = true;
    try {
      const res = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        body: formData
      });
      const data = await res.json();
      prediction = data.prediction;
    } catch (err) {
      console.error(err);
      prediction = 'Error';
    } finally {
      loading = false;
    }
  }
</script>
<div class="flex justify-center p-12 space-y-4 max-w-10xl">
    <div class="flex-col w-10/12 max-w-5xl text-center bg-gray-100 rounded-lg shadow-lg p-8">
        <h1 class="text-7xl font-bold mb-12">Test</h1>

        <div class="flex flex-col items-center gap-4 p-4 rounded-xl w-full max-w-md mx-auto shadow">

            
        <label for="fileInput" class="choose_image">Choose image</label>
        <input
            type="file"
            accept="image/*,.zip"
            on:change={handleFileChange}
            class="font-mono block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4
                file:rounded-full file:border-0 file:text-sm file:font-semibold
                file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
        />
        <button on:click="{handleSubmit}" disabled="{!file || loading}" class="mt-4 px-6 py-2 bg-blue-600 text-white rounded-lg shadow hover:bg-blue-700 disabled:opacity-50">
            {loading ? 'Predicting...' : 'Submit'}
        </button>


        {#if imagePreview}
            <img src={imagePreview} alt="Preview" class="mt-4 rounded-lg shadow max-h-64 object-contain" />
        {/if}

        {#if prediction}
            <p>Prediction: {prediction}</p>
        {/if}
        </div>
    </div>
</div>
