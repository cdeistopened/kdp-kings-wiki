import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

const config: QuartzConfig = {
  configuration: {
    pageTitle: "KDP Kings Wiki",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "en-US",
    baseUrl: "kdpkings.wiki",
    ignorePatterns: ["private", "templates", ".obsidian", "_templates"],
    defaultDateType: "created",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Space Grotesk",
        body: "Inter",
        code: "JetBrains Mono",
      },
      colors: {
        lightMode: {
          light: "#FAF6EF",
          lightgray: "#E0D9CC",
          gray: "#9B9890",
          darkgray: "#6F6E69",
          dark: "#1A1A1A",
          secondary: "#C8943E",
          tertiary: "#B07D2E",
          highlight: "rgba(200, 148, 62, 0.10)",
          textHighlight: "rgba(200, 148, 62, 0.20)",
        },
        darkMode: {
          light: "#1E1E1E",
          lightgray: "#333333",
          gray: "#6F6E69",
          darkgray: "#9B9890",
          dark: "#E8E4DD",
          secondary: "#C8943E",
          tertiary: "#D4A84E",
          highlight: "rgba(200, 148, 62, 0.12)",
          textHighlight: "rgba(200, 148, 62, 0.20)",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config
