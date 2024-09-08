# Scenarioviewer

[Svelte](https://svelte.dev/) implementation of the original scenario viewer made for 'Scenariostudie kernenergie' using `Dash`. In a nutshell, it allows a user to fetch only the results (figures, tables and key figures) of a selected scenario (set of constraints/parameters). It is a *completely* **static** build hosted on Azure Data Lake using the static website feature. All data is fetched from the datalake through the public `$web` container. This includes dropdowns, tables, descriptions, input options, etc. 

## CI/CD
The Svelte front-end is deployed using CI/CD as described in `azure-pipelines.yml`. 
1. Node is used to build using Vite
2. Svelte/Vite's static adapter delivers a `build` folder that entails the entire static build (including static resources)
3. Azure's Key Vault is used to fetch the Azure Data Lake credentials using the service principal. The SP is connected to the Azure Devops Repo and the Azure Resource Group. 
4. Python is used to push the entire build to the data lake, using the before mentioned creds (`connection_string`). This is implemented in `publish.py`.

## Data and figures
This repo does not include the data or figures that are displayed by the viewer. That part of the `ETL` is implemented in repo: `pypsa-datamanager`. This module is responsible for loading 'raw' result data (`.nc`) and transforming that to `Plotly`-figures in `json` format. Underlying data is also available by exporting the `Pandas.DataFrame` to `json` representation. Raw results are loaded from non-public containers, transformed and exported to the public `$web` container.


## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```bash
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```bash
npm run build
```

You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an [adapter](https://kit.svelte.dev/docs/adapters) for your target environment.
