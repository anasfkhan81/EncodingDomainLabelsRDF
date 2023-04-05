# Guidelines for Encoding Domain Labels for Linked Data Lexical Resources in RDF
###  Fahad Khan, Ana Salgado, Rute Costa, Margarida Ramos, Bruno Almeida, Sara Carvalho and Raquel Silva

- [Domain Labels – An Introduction](#domain-labels---an-introduction)
  * [Examples](#examples)
  * [Requirements](#requirements)
- [Best Practises for Encoding Domain Labels](#best-practises-for-domain-labels)
- [Examples](#examples-1)
  * [Namespaces](#namespaces)
  * [Encoding Hierarchical Domain Labels in the _Academia_ dictionary](#encoding-hierarchical-domain-labels-in-the--dicion-rio-da-academia-de-ci-ncias-)
  * [Encoding Hierarchical Domain Labels in the _Morais_ dictionary](#encoding-hierarchical-domain-labels-in-the--morais--dictionary)
- [Acknowledgements](#acknowledgements)
- [References](#references)



## Domain Labels – An Introduction

In the context of lexicography, the term _domain label_ is commonly used to denote usage labels[^1] assigned to senses as a ‘marker which identifies the specialised field of knowledge in which a lexical unit is mainly used’ (Salgado, Costa & Tasovac, 2019)[^2]. These labels are used ‘para señalar el léxico temáticamente especializado, en contraposición al léxico común’ [to signal the thematically specialised lexicon in contrast to the common lexicon] (Estopà, 1998, p. 1) and are generally expressed in the form of abbreviations, especially in paper dictionaries, representing individual domains.[^3] Therefore, thorough this work, we use the term domain label to indicate abbreviations (e.g., _Geograf._) collected in our dictionaries under analysis, but also to mention the extensions of each of the abbreviations written in full, e.g. GEOGRAFIA [GEOGRAPHY]).-->

[^1]: Although we will not go about detail into the broader topic of usage labels here, it is important to understand the association of such labels with a lexical unit implies that the label moves away ‘in a certain respect, from the main bulk of items described in a dictionary, and that its use is subject to some kind of restriction’ (Svensén, 2009, p. 313). The need to label certain deviations and restrictions in the use of a term (such as, for instance, when it is associated with a familiar register  or if it belongs to a specialised domain) originated in what is currently called _marking_ or _diasystematic marking_ (Hausmann, 1989, p. 651).  
[^2]: Note that the designation domain label is not universally accepted. Atkins and Rundell (2008), referring to ‘linguistic labels’, classified specialised vocabulary as ‘domains’ (p. 182); they are termed ‘field labels’ according to Verkuyl, Janssen and Jansen (2003, p. 7), ‘marcas técnicas’ by Fajardo (1996/1997), ‘marca de materia’ (Martínez de Sousa, 1995), ‘marca terminológica’ in Lara (1997), ‘marcas temáticas’ in Estopà (1998), ‘field label’ (Hartmann & James, 1998/2002), ‘marca de especialidad’ (Nomdedeu Rull, 2008), or ‘diatechnical information/marking’ (Hausmann, 1989; Svensén, 2009). We chose to use the term ‘domain label’ because we feel it is a transparent and recognisable designation for lexicographers, as well as a beacon for terminologists. 
[^3]: We define a domain as a ‘field of special knowledge’ (ISO 1087, 2019, p. 1):  this definition has the advantage of being both transparent and sufficiently comprehensive. Taking the complexity of domain knowledge into consideration, Sager (1990) states that ‘[i]n practice, no individual or group of individuals possesses the whole structure of a community’s knowledge; conventionally, we divide knowledge up into subject areas, or disciplines, which is equivalent to defining subspaces of the knowledge space.’ (p. 16). 

Although domain labels are commonly associated with individual lexical unit senses, they can also be assigned to individual entries (this is useful in case a term is only used in a technical sense) as well as other components of an entry. Domain labels can, moreover, be organised in taxonomies or thesauri, something that can help to make lexicons easier to navigate. Although such labels play an important role in lexical resources, and especially in lexicographic resources, there hasn’t been much work on modelling these as in linked data lexicons in a way that better exploits the possibilities of the Semantic Web stack (see Almeida et. al, 2022).  In the rest of this document we will present a series of guidelines for how to encode domain label information in RDF using three linked data vocabularies, namely OntoLex-Lemon, SKOS, and Lexicog. These will be illustrated by a series of examples taken from two Portuguese language dictionaries, one historic and the other contemporary. 


<!--The domain labelling, a particular dictionary feature, takes our attention through this research.--> 


<!--In the context of lexicography, the term domain label is often used to describe the assigned to senses are called domain labels, which are defined as a ‘marker which identifies the specialised field of knowledge in which a lexical unit is mainly used’ (Salgado, Costa & Tasovac, 2019). These labels are used ‘para señalar el léxico temáticamente especializado, en contraposición al léxico común’ [to signal the thematically specialised lexicon in contrast to the common lexicon] (Estopà, 1998, p. 1) and are generally expressed in the form of abbreviations (remember the economy of space rationale in the paper format).-->


<!--Meanwhile, we must recognise that, in general dictionaries, the usage of domain labels is neither entirely satisfactory nor consistently efficacious as it is applied with subjective criteria. Assigning domain labels to lexical units has always been a challenging issue for any lexicographer. In addition to the domain label, linguistic formulae are used in the definitions, contexts and other indicators to point to specialised meanings. They are faced with difficult decisions such as: What domain label should be assigned to this specific specialised meaning? Should a domain label be assigned to a meaning that once was specialised, but nowadays belongs to the common knowledge? These are decisions that the lexicographer takes in a solitary way. 
Assuming that the unmarked lexicon belongs to the general lexicon, as we shall see, is a controversial matter. In fact, not every lexical unit that can be considered a term is marked. It is unclear if this is due to forgetfulness or if the lexicographer decided to apply different criteria. In most cases, we can only limit ourselves to making assumptions, given the lack of introductory and explanatory texts in the dictionary on the methodology and criteria that have been followed. On the other hand, by comparing different lexicographic resources, we identify imbalanced criteria for selecting domains. The coexistence of generic domains with smaller spectrum domains is one of the problems.-->

### Examples
In what follows we will take our examples from the _Dicionário da Língua Portuguesa_ or DLP-ACL (ACL, 2023).
### Requirements
In the rest of the document we will assume a basic familiarity with the [OntoLex-Lemon vocabulary](https://www.w3.org/2016/05/ontolex/), the extension dealing with lexicographic resources the [OntoLex-Lemon Lexicography Module (Lexicog)](https://www.w3.org/2019/09/lexicog/), and the [Lexinfo vocabulary](https://lexinfo.net/) which allows for the addition of more specific linguistic information to RDF vocabularies (such as for instance part of speech information with respect to individual words). In addition, will also assume some familiarity with the [SKOS vocabulary](https://www.w3.org/TR/swbp-skos-core-spec/). 

## Best Practises for Encoding Domain Labels
The [original](https://lemon-model.net/)  LExicon Model for ONtologies (_lemon_) model, the immediate predecessor of OntoLex-Lemon allowed, for the addition of topic information to entries with the ```lemon:topic property``` as well as the use of ```lemon:context``` to specify the technical register of a sense.  OntoLex-Lemon does not contain these properties; instead, the [OntoLex-Lemon guidelines](https://www.w3.org/2016/05/ontolex/) do suggest the use of the ```dct:subject``` property to specify: 
> under which conditions (context, register, domain, etc) it is valid to regard the lexical entry as having the ontological entity as meaning.

The same guidelines also recommend the use of the ```ontolex:usage``` property which is defined as indicating: 
> usage conditions or pragmatic implications when using the lexical entry to refer to the given ontological meaning 

This property has the domain of ```ontolex:LexicalSense``` and the range ```rdfs:Resource```. Moreover, in the lexinfo vocabulary[^4] we have subproperties of ```ontolex:usage```, including ```lexinfo:domain``` which is defined as a: 
>usage marker which identifies the specialized field of knowledge in which a lexical unit is mainly used.

[^4]: Here and throughout this document when we mention lexinfo we are referring to [lexinfo 3.0](https://lexinfo.net/ontology/3.0/lexinfo).

Ontolex therefore offers us a way of marking a lexical entry as belonging to a certain domain and a way of specifying that a specific sense of an entry is associated with a particular domain.  When it comes to encoding the domain label itself, we suggest encoding it as a instance of the SKOS class ```Concept``` and using the ```skos:narrower``` and ```skos:broader``` relations to encode the relations between different domains. 

---
**SUMMARY OF RECOMMENDATIONS** 

We recommend the following steps when encoding domain label information in lexical resources:

1. Domain labels themselves should be encoded as individuals of the class ```skos:Concept```. Hierarchical relationships between individual domain labels should be encoded using the ```skos:narrower``` and ```skos:broader``` properties. In the case of retrodigitised and non-native born dictionaries, it may be that the same domain label is not consistently encoded using the same string; in such situations we recommend using ```skos:preflabel``` and ```skos:altlabel``` to list the different versions of the same label (with the former being used to encode the version(s) found in the front matter and the latter its variants).
2. In case the whole entry is marked as (or interpreted by the encoder as) belonging to a given domain we recommend encoding this information using ```dcterms:subject``` with the entry as subject and the relevant domain label (encoded as ```skos:Concept```, see above) as object.  
3. In case a single sense is marked as (or is interpreted by the encoder as) belonging to a domain we recommend using ```lexinfo:domain``` with the entry as subject and the relevant ```skos:Concept``` as object.
4. In other cases where any other part of the entry is marked with a domain label, once again we recommend the use of ```dcterms:subject```.
---


<!--- In the following examples, we will look at how to encode several different kinds of examples of domain labels, trying to capture several different varieties of use case:
When the meaning specified refers to a specific technical sense of a word belonging to a domain **we recommend using the ```ontolex:LexicalConcept``` class** --->
## Examples

### Namespaces
In the examples that follow we use the following namespaces:

      @prefix lexinfo: <http://www.lexinfo.net/ontology/3.0/lexinfo#> .
      @prefix ontolex: <http://www.w3.org/ns/lemon/ontolex#> .
      @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
      @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
      @prefix dcterms: <http://purl.org/dc/terms/> .
      @prefix lexicog: <http://www.w3.org/ns/lemon/lexicog#> .
      

### Encoding hierarchical domain labels in the _Dicionário da Academia de Ciências_

In the first example, we show how to encode an entry which has a sense that has been marked with a domain label and where the domain referred to is part of a hierarchy of domains. In this case the entry is for the Portuguese lexical unit _cristalografia_ 'crystallography' from the DLP-ACL. As the following figure shows, this entry has one sense which is marked with the label MINERALOGIA referring to the domain of mineralogy. 

![Cristalografia Example![cristalografia_DLP](https://user-images.githubusercontent.com/45368069/227588665-33146354-1dd5-4497-9594-f5c1567008e9.png)
](Examples/cristalografia_DLP.png "Cristalografia Example")
<!--![Cristalografia Example](Examples/cristalografia_DLP.png "Cristalografia Example")-->

Some additional information relevant for this example is that the domain of MINERALOGIA is a subdomain of GEOLOGIA 'geology' in the DLP-ACL subject hierarchy that has CIÊNCIAS DA TERRA 'earth sciences' has a superdomain.   

We can represent these domains and their interrelations as follows using the SKOS vocabulary:

      <http://example.org/class/mineralogia> rdf:type  skos:Concept; 
        skos:prefLabel "mineralogia"@pt;
        skos:prefLabel "minerology"@en; 
        skos:narrower <http://example.org/class/geologia> .
      <http://example.org/class/geologia> rdf:type  skos:Concept; 
          skos:prefLabel "geologia"@pt;
          skos:prefLabel "geology"@en; 
          skos:narrower <http://example.org/class/ciencas_da_terra> ;
          skos:broader <http://example.org/class/mineralogia> .
      <http://example.org/class/ciencias_da_terra> rdf:type  skos:Concept;
          skos:prefLabel "ciencias da terra"@pt;
          skos:prefLabel "earth sciences"@en; 
          skos:broader <http://example.org/class/mineralogia> .


In the entry itself, we link the (single) sense of the entry for _cristalografia_ (note that the sense is a blank node in the current example) to the domain ```<http://example.org/class/mineralogia>``` via the ```lexinfo:domain``` property.

      <http://example.org/class/DLP_cristalografia> a ontolex:LexicalEntry ;
       lexinfo:etymology [ rdf:value "Do grego κρύσταλλος cristal + sufixo -grafia"@pt ] ;
       lexinfo:gender lexinfo:feminine ;
       lexinfo:partOfSpeech lexinfo:noun ; 
        ontolex:canonicalForm [ 
                            ontolex:phoneticRep "kriʃtɐluɡrɐˈfiɐ"@pt ;
                            ontolex:writtenRep "cristalografia"@pt 
                            ] ;
         ontolex:sense [ lexinfo:domain <http://example.org/class/mineralogia>;
                           skos:definition """ciência que estuda os cristais, considerando aspetos tais como o seu crescimento, a
                           estrutura interna e as propriedades físicas decorrentes da regularidade dessa estrutura,
                           em particular, as formas que apresentam, cuja simetria utiliza como método de
                           classificação e de descrição"""@pt ] .



### Encoding hierarchical domain labels in the _Morais_ dictionary
Our second example is derived from the encoding of a retrodigitised dictionary, Morais,  in which we have the use of variants for the same domain label. We will look at two individual entries in what follows. The first is the entry for the polysemic word _axe_ 'pimple, axle' and the second is the entry for _citerior_  'on the near side of something'. Both are shown in the figures below. 

![Axe Example](https://github.com/anasfkhan81/EncodingDomainLabelsRDF/blob/13d34e20ef3b7f85947240c254d563f03f74d99d/Examples/AXE_morais1.png)

![Citerior Example](https://github.com/anasfkhan81/EncodingDomainLabelsRDF/blob/13d34e20ef3b7f85947240c254d563f03f74d99d/Examples/CITERIOR_morais1.png)

Both of these entries include a domain label pertaining to the domain of geography. In the first entry this is referred to as "t. Geograf."; in the second example "Geograf." We encode this domain label as follows:


      <http://example.org/class/geografia> rdf:type  skos:Concept ; 
          skos:prefLabel "t. Geograf."@pt;
          skos:altLabel "Geograf."@pt. 

Note here the two different labels for the domain, with 't.Geograf' as the preferred label (since it is listed in the dictionary's front matter).

Moving onto the entry for _axe_, we can encode it as follows:

      <http://example.org/individual/MORAIS.1.DLP.AXE> a ontolex:LexicalEntry ;
          lexinfo:gender lexinfo:masculine ;
          lexinfo:partOfSpeech lexinfo:noun ; 
          ontolex:canonicalForm [ ontolex:writtenRep "AXE"@pt ] ;
          ontolex:sense [ 
                          lexinfo:socioCultural [ rdf:value "ch." ] ;
                          skos:definition "feridinha, borbulhinha"@pt 
                         ],
                         [ 
                          lexinfo:domain <http://example.org/class/geografia> ;
                          skos:definition "eixo"@pt ;
                          lexicog:usageExample [ dcterms:source "C. Eleg. O Poeta Simonides . ";
                              rdf:value "Dando do segundo axe certa prova"@pt ]; 
                          lexicog:usageExample [ dcterms:source "Luſ. . 10. 87. . "]
                          ] .

Note that the entry has two different senses (both of these blank nodes)[^5]. The second sense is the relevant one in our case; note also the two usage examples associated with the sense. Once again we use the ```lexinfo:domain```[^6]. 



    <http://example.org/instance/MORAIS.1.DLP.CITERIOR> a ontolex:LexicalEntry ;
        ontolex:canonicalForm [ ontolex:writtenRep "CITERIOR"@pt ] ;
        lexinfo:partOfSpeech lexinfo:adjective ; 
        ontolex:sense [ 
                    skos:definition "que fica áquem de algum poſto, ou ſitio"@pt ;
                    lexicog:usageExample [ 
                                dcterms:source "  M. Luſ. ,, usa-se na t. Geograf. Hespanha citerior, e ulterior . "; 
                                dcterms:subject  <http://example.org/class/geografia>] ] .

Note that in this case we associate the domain label with the usage example rather than the entry or even the sense, making use, in this case of ```dcterms:subject```.  

[^5]: We can order these two senses using the ```lexicog:LexicographicComponent```class, see [the lexicog guidelines](https://www.w3.org/2019/09/lexicog/#example4). We decided not to do this in the current case in the interests of keeping the exposition as simple as possible. 
[^6]: In order to keep the example simple we haven't added any structured bibliographic information, even though this can be easily done using a number of linked data vocabularies such as [...]. 

## Acknowledgements
This work presented here was supported by a short term scientific mobility grant from the COST Action
NexusLinguarum (CA18209) supported by COST
(European Cooperation in Science and Technology). It was also supported by the MORDigital – Digitalização do Diccionario da Lingua
Portugueza de António de Morais Silva [PTDC/LLT-LIN/6841/2020] project financed by the Portuguese National Funding through the FCT – Fundação para a Ciência e Tecnologia 

## References

Svensén, B. (2009). A Handbook of Lexicography: The Theory and Practice of Dictionary Making. Cambridge: Cambridge University Press.
Almeida, B., Costa, R., Salgado, A., Ramos, M., Romary, L., Khan, F., ... & Tasovac, T. (2022). Modelling Usage Information in a Legacy Dictionary: From TEI Lex-0 to Ontolex-Lemon.

Hausmann, F. J. (1989). Die Markierung in eineim allgemeinen einsprachigen Wörterbuch: eine Übersicht. In F. J. Hausmann, O. Reichmann, H. E. Wiegand, L. Zgusta (Eds.), Wörterbücher. Ein internationales Handbuch zur Lexikographie (pp. 649–657). Berlin: Walter de Gruyter.

Salgado, A., Costa, R. & Tasovac, T. (2019). Improving the consistency of usage labelling in dictionaries with TEI Lex-0. Lexicography: Journal of ASIALEX, 6(2), 133–156. doi:10.1007/s40607-019-00061-x.

Estopà, R. B. (1998). El léxico especializado en los diccionarios de lengua general: las marcas temáticas. Revista de la Sociedad Española de Linguística, 28(2), 359–387.

Atkins, B. T. S., & Rundell, M. (2008). The Oxford Guide to Practical Lexicography. New York: Oxford University Press.

Verkuyl, H. J., Janssen, M., & Jansen, F. (2003). The codification of usage by labels. In Sterkenburg, P. (Ed.), A practical guide to lexicography (pp. 297–311). Amsterdam: John Benjamins. doi:10.1075/tlrp.6.33ver.

Sager, J. C. (1990). A practical course in terminology processing. Amsterdam: John Benjamins Publishing Company.

ISO 1087. (2019). Terminology Work – Vocabulary – Part 1: Theory and Application. Geneva: International Organization for Standardization.

Almeida, B., Costa, R., Salgado, A., Ramos, M., Romary, L., Khan, F., Carvalho, S., Khemakhem, M., Silva, R., & Tasovac, T. (2022). Modelling Usage Information in a Legacy Dictionary: From TEI Lex-0 to Ontolex-Lemon.


Morais Silva, A. M. (1789). Diccionario da lingua portugueza composto pelo padre D. Rafael Bluteau, reformado, e accrescentado por Antonio de Moraes Silva, natural do Rio de Janeiro (Vol. 1–2). Officina 730 de Simão Thaddeo Ferreira. https://purl.pt/29264.

ACL (2023). Dicionário da Língua Portuguesa. Salgado, A. (Coord.). Lisboa: Academia das Ciências de Lisboa. https://dicionario.acad-ciencias.pt/

