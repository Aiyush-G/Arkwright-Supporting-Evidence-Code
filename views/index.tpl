<!-- default theme 👇 -->
<html data-theme="light">
<!-- try other themes 👇 -->
<!-- [dark, light, black, cyberpunk, dracula, valentine, retro, synthwave, garden, halloween, aqua, cupcake, bumblebee, pastel, forest, fantasy, luxury] -->
<!-- more info: https://daisy.js.org/docs/default-themes -->
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=yes">
  <title>{{ webTitle }}</title>
  <link href="static/tailwind.min.css" rel="stylesheet" type="text/css" />
  <link href="static/daisy.css" rel="stylesheet" type="text/css" />
  
  <!-- this script is for changing and saving theme -->
  <script src="static/select.js"></script>
  <body>
    <!-- put everything in a off-canvas drawer -->
   
    <!-- OLD.HTML -->
    <div class="h-screen bg-base-200 drawer text-base-content">
        <!-- this checkbox controls if drawer is open -->
        <input id="menu-drawer" type="checkbox" class="drawer-toggle" />
        <div class="flex flex-col drawer-content">
          <!-- drawer content -->
          <div class="w-full navbar bg-base-300">
            <!-- hamburger menu is only visible on mobile -->
            <div class="flex-none lg:hidden">
              <label for="menu-drawer" class="btn btn-square btn-ghost">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  class="inline-block w-6 h-6 stroke-current"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M4 6h16M4 12h16M4 18h16"
                  ></path>
                </svg>
              </label>
            </div>
            <div class="flex-1 px-2 mx-2 font-bold">
              <!-- navbar title -->
              <span>{{ pageTitle }}</span>
            </div>
            <div class="flex-none">
              <!-- navbar is only visible for desktop -->
              <div class="hidden lg:inline-block">
                <ul class="mr-2 space-x-2 menu horizontal">
                  <li>
                    <a href="#" class="rounded-btn">Home</a>
                  </li>
                  <li>
                    <a target="_blank" href="#" class="rounded-btn">Plant Dude</a>
                  </li>
                </ul>
              </div>
              <select class="select" data-choose-theme>
                <option value="">Change Theme</option>
                <option value="dark">dark</option>
                <option value="light">light</option>
                <option value="black">black</option>
                <option value="cyberpunk">cyberpunk</option>
                <option value="dracula">dracula</option>
                <option value="valentine">valentine</option>
                <option value="retro">retro</option>
                <option value="synthwave">synthwave</option>
                <option value="garden">garden</option>
                <option value="halloween">halloween</option>
                <option value="aqua">aqua</option>
                <option value="cupcake">cupcake</option>
                <option value="bumblebee">bumblebee</option>
                <option value="pastel">pastel</option>
                <option value="forest">forest</option>
                <option value="fantasy">fantasy</option>
                <option value="luxury">luxury</option>
              </select>
            </div>
          </div>
          <!-- main content -->
          <div class="flex h-screen justify-center items-center">
            <div class="w-full max-w-md p-4 text-center place-items-center">
              <!-- avatar -->
              <div class="mx-auto avatar mt-28">
                <div class="w-32 h-32 p-1 mb-8 mask mask-squircle bg-secondary">
                  <img src="{{ image }}" class="mask mask-squircle" />
                </div>
              </div>
              <!-- text -->
              <div class="pb-3">
                <h1 style="text-transform: capitalize;" id="title" class="py-2 text-2xl font-bold">{{ ff}}</h1>
                
                <p class="text-sm text-opacity-70 text-base-content">
                  {{ shortDesc }}
                </p>
              </div>
              <!-- stats -->
              
              <div class="my-3 shadow stats">
                  <div class="stat">
                    <div class="stat-title">Temperature °C</div> 
                    <div class="stat-value">{{ temperature }}</div> 
                    <div class="stat-desc">Updated Every 5 Minutes</div>
                  </div>
              </div>
              
              
              <div class="shadow stats">
                  <div class="stat">
                    <div class="stat-title">Humidity</div> 
                    <div class="stat-value">{{ humidity }}%</div> 
                    <div class="stat-desc">This is ±5%</div>
                  </div>
              </div>

              <div>
                <form action="/" method="post">
                
                  <div class="card shadow">
                    <div class="stat">
                        <div class="stat-value">Speaker Volume</div> 
                        <br>
                        <input name="speakerVolume" type="range" max="100" value="{{speakerVolume}}" class="range range-primary"> 
                    </div>
                  </div> 

                  <br>

                  <input type="submit" name="LED" class="btn btn-accent" value="Lighting"/>
                  <input type="submit" name="speaker" class="btn btn-accent" value="Speaker"/>
                  <input type="submit" name="speakerVolumeUpdate" class="btn btn-accent" value="Update Volume"/>

                  
                  <div class="py-3 px-3">
                    <input type="submit" name="howToUse" class="btn btn-accent mx-3 my-3" value="How to Use"/>
                    <input type="submit" name="forcast" class="btn btn-accent mx-3 my-3" value="Local Forcast"/>
                    <input type="submit" name="restart" class="btn btn-primary mx-3 my-3" value="Kill Engine"/>
                    <input type="submit" name="disco" class="btn btn-neutral mx-3 my-3" value="Music Mode"/>
                  </div>

                
                  


                  
                  
                </form>
              </div>
    
              <div class="py-3">
                  <!--<a target="_blank" class="btn btn-primary" href="https://daisy.js.org/">Learn More</a>-->
                  <label for="my-modal-2" class="btn btn-primary modal-button">Learn Even More!</label> 
                  <input type="checkbox" id="my-modal-2" class="modal-toggle"> 
                  <div class="modal">
                    <div class="modal-box">
                      <p>{{ longDesc }}</p> 
                      <div class="modal-action">
                        <label for="my-modal-2" class="btn btn-primary">Close</label> 
                        <!--<label for="my-modal-2" class="btn">Close</label>-->
                      </div>
                    </div>
                  </div>
              </div>
            </div>
          </div>
        </div>
        <!-- drawer sidebar for mobile -->
        <div class="drawer-side">
          <label for="menu-drawer" class="drawer-overlay"></label>
          <ul class="p-4 overflow-y-auto menu w-80 bg-base-100">
            <li>
              <a href="#">Home</a>
            </li>
            <li>
              <a target="_blank" href="https://daisy.js.org/">DaisyUI</a>
            </li>
          </ul>
        </div>
      </div>

  </body>
</html>