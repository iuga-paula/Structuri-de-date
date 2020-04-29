#include <iostream>
#include <fstream>
using namespace std;

//Fiecare drum simplu de la un nod la un descendent care este frunza contine acelasi numar de noduri negre

ifstream in ("abce.in");  //fiser cu operatiile de executat asupra arborilor cate una pe rand
ofstream out("abce.out");

typedef struct Nod
{
    int valoare;
    Nod *parinte;
    Nod *stanga;
    Nod *dreapta;
    int culoare; //0 pt rosu, 1 pt negru

}*NodRN; //sa ca folosesc NodRN la la declarari in loc de Nod* ...

class Arbore_rosu_negru
{
private:
    NodRN radacina;
    NodRN NodNULL;

public:
    Arbore_rosu_negru()  //constructor
    {
        NodNULL = new Nod;
        NodNULL ->culoare = 0; //nod rosu
        NodNULL ->dreapta = nullptr;
        NodNULL ->stanga = nullptr;
        radacina = NodNULL;


    }

    NodRN get_radacina()
    {
        return this -> radacina;
    }

    int cauta_val(NodRN nod, int val) //returneaza 1 dacă valoarea exista în structura și 0 altfel
    {
        if(nod == NodNULL)
            return 0;
        if(nod->valoare == val)
            return 1;

        int subarbore_stang = cauta_val(nod->stanga,val);
        if (subarbore_stang)
            return 1;
        int subarbore_drept = cauta_val(nod->dreapta,val);
        return subarbore_drept;

    }


    void inordine(NodRN nod, int x, int y)  //afiseaza crescator elem din intervalul [x,y]
    {
        if(nod != NodNULL && nod->valoare >= x && nod->valoare <=y)
        {
            inordine(nod->stanga, x, y);
            out<<nod->valoare<<" ";
            inordine(nod->dreapta, x, y);
        }

    }

    NodRN cauta_nod(NodRN nod, int val)
    {


        if(nod == NodNULL)
            return NodNULL;
        if(nod->valoare == val)
            return nod;

        NodRN subarbore_stang = cauta_nod(nod->stanga,val);
        if (subarbore_stang != NodNULL)
            return subarbore_stang;
        NodRN subarbore_drept = cauta_nod(nod->dreapta,val);
        return subarbore_drept;


    }

    int succesor(int val)   // cea mai mica valoare din arbore >=  val nod
    {
        NodRN a = cauta_nod(radacina, val);
        if(a->dreapta != NodNULL) // Dacă am fiu drept atunci cel mai mic element va fi cel mai mic element din subarborele drept. Adică dreapta->stânga->stânga-> … -> stânga
        {
            NodRN nod = a->dreapta;
            while(nod->stanga != NodNULL)
            {
                nod = nod ->stanga;
            }
            return nod->valoare;
        }
        NodRN b = a ->parinte;// Daca nu am fiu drept atunci va fi primul stramos al meu în care eu sunt în subarborele stang al sau.
        while( b != NodNULL && a==b->dreapta)
        {
            a = b;
            b = b->parinte;
        }
        return b->valoare;

    }


    int predecesor(int val)//cea mai mare valoare din arbore <= val nod
    {

        NodRN a = cauta_nod(radacina, val);
        if( a->stanga != NodNULL)//Dacă am fiu stang atunci cel mai mic element va fi cel mai mic element din subarborele stang. Adică stanga->dreapta->dreapta-> …
        {
            NodRN nod = a->stanga;
            while(nod->dreapta != NodNULL)
            {
                nod = nod->dreapta;
            }
            return nod->valoare;
        }

        NodRN b = a->parinte; //Daca nu am fiu stang atunci va fi primul stramos al meu în care eu sunt în subarborele drept al sau.
        while(b != NodNULL && a == b->stanga)
        {
            a = b;
            b = b->parinte;
        }

        return b->valoare;
    }

    void rotatie_stanga(NodRN nod)
    {
        NodRN a = nod->dreapta;
        nod->dreapta = a->stanga;
        if(a->stanga != NodNULL)
        {
            a->stanga->parinte = nod;
        }
        a->parinte = nod->parinte;

        if(nod->parinte == nullptr)
            this->radacina = a;
        else if( nod == nod->parinte->stanga)
        {
            nod->parinte->stanga = a;
        }
        else
        {
            nod->parinte->dreapta = a;
        }
        a->stanga = nod;
        nod->parinte = a;

    }

    void rotatie_dreapta(NodRN nod)
    {
        NodRN a = nod->stanga;
        nod->stanga = a->dreapta;
        if(a->dreapta != NodNULL)
        {
            a->dreapta->parinte = nod;
        }
        a->parinte = nod->parinte;
        if(nod->parinte == nullptr)
            this->radacina = a;
        else if( nod == nod->parinte->dreapta)
        {
            nod->parinte->dreapta = a;
        }
        else
        {
            nod->parinte->stanga = a;
        }
        a->dreapta = nod;
        nod->parinte = a;

    }



    void inserarefixa(NodRN nod)
    {
        NodRN nod1;
        while(nod->parinte->culoare == 1) //pana cand parintele nodului este rosu
        {
            if(nod->parinte == nod->parinte->parinte->dreapta)
            {
                nod1 = nod->parinte->parinte->stanga;
                if(nod1->culoare == 1)
                {
                    nod1->culoare = 0;
                    nod->parinte->culoare = 0;
                    nod->parinte->parinte->culoare = 1;
                    nod = nod->parinte->parinte;
                }
                else
                {
                    if(nod == nod->parinte->stanga)
                    {
                        nod = nod->parinte;
                        rotatie_dreapta(nod);
                    }
                    nod->parinte->culoare = 0;
                    nod->parinte->parinte->culoare = 1;
                    rotatie_stanga(nod->parinte->parinte);

                }
            }
            else
            {

                nod1 = nod->parinte->parinte->dreapta; //daca copilu drept al strabunicului
                if(nod1->culoare == 1)
                {
                    nod1->culoare =0;
                    nod->parinte->culoare = 0;
                    nod->parinte->parinte->culoare = 1;
                    nod = nod->parinte->parinte;

                }
                else                      //este rosu
                {
                    if(nod == nod->parinte->dreapta)
                    {
                        nod = nod->parinte;
                        rotatie_stanga(nod);
                    }
                    nod->parinte->parinte->culoare = 1; //copii devin negri
                    rotatie_dreapta(nod->parinte->parinte);
                }
            }
            if(nod == radacina)
                break;

        }
        radacina->culoare = 0;
    }

    void inserare(int valoare)
    {
        NodRN nod = new Nod;   //se creaza un nou nod de culoare neagra
        nod->parinte = nullptr;
        nod->valoare = valoare;
        nod->stanga = NodNULL;
        nod->dreapta = NodNULL;
        nod->culoare = 1;

        NodRN y = nullptr; //y frunza
        NodRN x = this->radacina;  //x radacina

        while( x!= NodNULL) //cat timp x nu e frunza(arborele nu e gol)
        {
            y = x;
            if(nod->valoare < x->valoare)//daca valoarea nodului de inserat este mai mica decat valoarea "radacinii"
            {
                x = x->stanga;//parcurgem subarborele stang pt a gasi locul noului nod
            }
            else
            {
                x = x->dreapta;  //alfel parcurgem subarborele drept
            }
        }

        nod->parinte = y; //parinte frunzei pe care am ajuns devine parintele noului nod
        if(y == nullptr)
        {
            radacina = nod;//daca arborele e vid se insereaza noul nod pe post de radacina(are culoarea neagra)
        }
        else if(nod->valoare < y->valoare)//daca valoarea frunzei e mai mare decat valoarea noului nod
        {
            y ->stanga = nod; //noul nod devine copilul drept al frunzei
        }
        else
        {
            y->dreapta = nod; //altfel devine copilul stang al frunzei
        }

        if(nod->parinte == nullptr)
        {
            nod->culoare = 0;  //coloram noul nod in rosu
            return;
        }
        if(nod->parinte->parinte ==nullptr)
            return;

        inserarefixa(nod);  //se apeleaza algoritmul de inserare fixa pt a vedea si repara daca noua inserare strica proprietatea de arbore rosu-negru
    }


    void transfer(NodRN a, NodRN b)
    {
        if (a->parinte == nullptr)
    {
      radacina = b;
    }
    else if (a == a->parinte->stanga)
    {
      a->parinte->stanga = b;
    }
    else
    {
      a->parinte->dreapta = b;
    }
    b->parinte = a->parinte;
    }

    void stergerefixa(NodRN a)
  {
    NodRN b;
    while (a != this->radacina && a->culoare == 0)
    {
      if (a == a->parinte->stanga)
      {
        b = a->parinte->dreapta;
        if (b->culoare == 1)
        {
          b->culoare = 0;
          a->parinte->culoare = 1;
          rotatie_stanga(a->parinte);
          b = a->parinte->dreapta;
        }

        if (a->stanga->culoare == 0 && b->dreapta->culoare == 0)
        {
          b->culoare = 1;
          a = a->parinte;
        }
        else
        {
          if (b->dreapta->culoare == 0)
          {
            b->stanga->culoare = 0;
            b->culoare = 1;
            rotatie_stanga(b);
            b = a->parinte->dreapta;
          }

          b->culoare = a->parinte->culoare;
          a->parinte->culoare = 0;
          b->dreapta->culoare = 0;
          rotatie_dreapta(a->parinte);
          a = radacina;
        }
      }
      else
      {
        b = a->parinte->stanga;
        if (b->culoare == 1)
        {
          b->culoare = 0;
          a->parinte->culoare = 1;
         rotatie_dreapta(a->parinte);
          b = a->parinte->stanga;
        }

        if (b->dreapta->culoare == 0 && b->dreapta->culoare == 0)
        {
          b->culoare = 1;
          a = a->parinte;
        }
        else
        {
          if (b->stanga->culoare == 0)
          {
            b->dreapta->culoare = 0;
            b->culoare = 1;
            rotatie_stanga(b);
            b = a->parinte->stanga;
          }

          b->culoare = a->parinte->culoare;
          a->parinte->culoare = 0;
          b->stanga->culoare = 0;
          rotatie_dreapta(a->parinte);
          a = radacina;
        }
      }
    }
    a->culoare = 0;
  }


    void stergere(int val)
    {
        NodRN nod = this->radacina;
        NodRN a = NodNULL;
        NodRN b, c;
        while (nod != NodNULL)
        {
            if (nod->valoare == val)
            {
                a = nod;
            }

            if (nod->valoare <= val)
            {
                nod = nod->dreapta;
            }
            else
            {
                nod = nod->stanga;
            }
        }

        if (a == NodNULL)
        {
            out <<"nodul cu valoarea data nu exista in arbore" <<"\n";
            return;
        }

        c = a;
        int c_culoare = c->culoare;
        if (a->stanga == NodNULL)
        {
            b = a->dreapta;
            transfer(a, a->dreapta);
        }
        else if (a->dreapta == NodNULL)
        {
            b = a->stanga;
            transfer(a, a->stanga);
        }
        else
        {
            a = a->dreapta;
            while(a->stanga != NodNULL)
            {
                a = a->stanga;
            }
            c_culoare =c->culoare;
            b = c->dreapta;
            if (c->parinte == a)
            {
                b->parinte = c;
            }
            else
            {
                transfer(c, c->dreapta);
                c->dreapta = a->dreapta;
                c->dreapta->parinte = c;
            }

            transfer(a, c);
            c->stanga = a->stanga;
            c->stanga->parinte = c;
            a->culoare = a->culoare;
        }
        delete a;
        if (c_culoare == 0)
        {
            stergerefixa(b);
        }
    }

};


int main()
{
    Arbore_rosu_negru arbore;
    //NodRN nod;
    int op,val, val2 = 0,n;
    in>>n;
    while(in>>op>>val)
    {
        switch(op)
        {
        case 1:
            cout<<"inserare valoarea ";
            cout<<val<<"\n";
            arbore.inserare(val);
            break;
        case 2:
            cout<<"sterge toate aparitiile lui ";
            cout<<val<<"\n";
            arbore.stergere(val);
            break;
        case 3:
            cout<<"cauta valoarea ";
            cout<<val<<"\n";
            out<<arbore.cauta_val(arbore.get_radacina(),val)<<"\n";
            break;
        case 4:
            cout<<"afiseaza succsesorul lui ";
            cout<<val<<"\n";
            break;
            out<<arbore.succesor(val)<<"\n";
        case 5:
            cout<<"afiseaza predecesorul lui";
            cout<<val<<"\n";
            out<<arbore.predecesor(val)<<"\n";
            break;

        case 6:
            in>>val2;
            cout<<"afiseaza toate valorile din intervalul ";
            cout<<val<<" "<<val2<<"\n";
            arbore.inordine(arbore.get_radacina(), val, val2);
            out<<"\n";
            break;
        default:
            cout<<"operatie necunoscuta!"<<"\n";
            out<<"operatie necunoscuta!"<<"\n";

        }
    }


    return 0;
}
