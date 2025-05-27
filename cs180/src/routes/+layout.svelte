<script lang="ts">
	import '../app.css';
	
	let { children } = $props();
</script>

<nav style="background-color: #623e2a;">
  <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8" >
    <div class="relative flex h-16 items-center justify-between">
      <div class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">
        <div class="hidden sm:ml-6 sm:block">
          <div class="flex space-x-4">
            <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
            <a href="/" class="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-amber-800 hover:text-white">Homepage</a>
            <a href="/modelA" class="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-amber-800 hover:text-white">Model A</a>
            <a href="/modelB" class="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-amber-800 hover:text-white">Model B</a>
            <a href="/test" class="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-amber-800 hover:text-white">Test Model</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</nav>


{@render children()}
