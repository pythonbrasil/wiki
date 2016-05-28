bootstrapify
===================================

This [pelican](https://github.com/getpelican/pelican) plugin modifies article and page html to use bootstrap's default classes. This is especially handy if you want to write tables in markdown, since the `attr_list` extension does not play nice with `tables`.

#Requirements
*   Beautifulsoup4 - install via `pip install beautifulsoup4`

#Features
*   Adds `table table-striped table-hover` to all `<table>` elements.
*   Adds `img-responsive` to all `<img>` elements.
*   Use `BOOTSTRAPIFY` in your Pelican configuration file to pass a `{'css-selector': ['list-of-classes']}` dictionary to the plugin. Bootstrapify will append `list-of-classes` to all tags that match `css-selector`. The selector can be as simple as a tag name (`table` or `p`) or as complicated as `a.menu:nth-of-type(3)` (see the [Beautifulsoup4 documentation](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors)).

#Example for md tables
1. Write your table in markdown

    ```
    | Protocol       | Contact Information
    |:-------------- |:-----------------------------------------------------|
    | jabber/xmpp    | [winlu@jabber.at](winlu@jabber.at)                   |
    | email          | [derwinlu@gmail.com](mailto:derwinlu@gmail.com)      |
    | IRC - freenode | winlu                                                |
    ```


2. there is no step 2, the plugin adds the needed classes to the `<table>` node, resulting in the following output:


    ```
    <table class="table table-striped table-hover">
    <thead>
    <tr>
    <th align="left">Protocol</th>
    <th align="left">Contact Information</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td align="left">jabber/xmpp</td>
    <td align="left"><a href="winlu@jabber.at">winlu@jabber.at</a></td>
    </tr>
    <tr>
    <td align="left">email</td>
    <td align="left"><a href="mailto:derwinlu@gmail.com">derwinlu@gmail.com</a></td>
    </tr>
    <tr>
    <td align="left"><span class="caps">IRC</span> - freenode</td>
    <td align="left">winlu</td>
    </tr>
    </tbody>
    </table>
    ```


#Known Issues
*   plugin seems not to fire for drafts
*   not enough customization possible, maybe read article,page metadata for more options
